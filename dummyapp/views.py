# dummyapp/views.py

import aiohttp
import asyncio
from rest_framework.response import Response
from rest_framework.views import APIView


class ConcurrentApiCall(APIView):

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


class ConcurrentFunctionCall(APIView):

    async def add(self, data):
        a = data['a']
        b = data['b']
        await asyncio.sleep(20)
        result = a + b
        return {'add_result': result}

    async def sub(self, data):
        a = data['a']
        b = data['b']
        result = a - b
        return {'sub_result': result}

    async def mul(self, data):
        a = data['a']
        b = data['b']
        await asyncio.sleep(5)
        result = a * b
        return {'mul_result': result}

    async def divide(self, data):
        a = data['a']
        b = data['b']

        if b == 0:
            return {'error': 'Division by zero is not allowed'}
        result = a / b
        return {'divide_result': result}

    async def concurrent_requests(self, data):
        tasks = [
            self.add(data),
            self.sub(data),
            self.mul(data),
            self.divide(data),
        ]

        # Use asyncio.gather to run the functions concurrently
        results = await asyncio.gather(*tasks)
        return results

    async def async_post(self, request):
        input_data = {'a': 5, 'b': 7}  # Example input values
        # Make concurrent function calls
        results = await self.concurrent_requests(input_data)

        # Return a Response object
        return Response(results)

    def post(self, request):
        # Call the asynchronous function using await
        return asyncio.run(self.async_post(request))
