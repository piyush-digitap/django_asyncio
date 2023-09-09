# dummyapp/views.py

import aiohttp
import asyncio
from rest_framework.response import Response
from rest_framework.views import APIView


class ConcurrentApiView(APIView):

    async def get_data_from_api(self, url, payload=None, headers=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, json=payload,
                                   headers=headers) as response:
                return await response.json()

    async def concurrent_requests(self):
        api_urls = [
            'https://jsonplaceholder.typicode.com/posts',
            'https://jsonplaceholder.typicode.com/comments',
            'https://jsonplaceholder.typicode.com/users',
            'https://jsonplaceholder.typicode.com/todos',
        ]

        payload = {'key': 'value'}  # Replace with your payload data
        headers = {
            'Authorization': 'Bearer your_token'
        }  # Replace with your authentication headers

        tasks = [
            self.get_data_from_api(url, payload=payload, headers=headers)
            for url in api_urls
        ]

        # Use asyncio.gather to concurrently fetch data from the APIs
        results = await asyncio.gather(*tasks)
        return results

    async def async_post(self, request):
        # Make concurrent API requests
        results = await self.concurrent_requests()

        # Process the results as needed
        # For demonstration purposes, we're returning the results as a list of responses
        response_data = results

        # Return a Response object
        return Response(response_data)

    def post(self, request):
        # Call the asynchronous function using await
        return asyncio.run(self.async_post(request))
