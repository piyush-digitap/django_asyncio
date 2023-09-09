import asyncio
from rest_framework.response import Response
from rest_framework.views import APIView


class ConcurrentApiView(APIView):

    async def add(self, data):
        a = data['a']
        b = data['b']
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
