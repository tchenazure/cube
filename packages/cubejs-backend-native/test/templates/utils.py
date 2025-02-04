from cube import context_func

@context_func
def arg_sum_integers(a, b):
  return a + b

@context_func
def arg_bool(a):
  return a + 0

@context_func
def arg_str(a):
  return a

@context_func
def arg_null(a):
  return a

@context_func
def load_data_sync():
   client = MyApiClient("google.com")
   return client.load_data()

@context_func
async def load_data():
   client = MyApiClient("google.com")
   return client.load_data()

class MyApiClient:
  def __init__(self, api_url):
    self.api_url = api_url

  # mock API call
  def load_data(self):
    api_response = {
      "cubes": [
        {
          "name": "cube_from_api",
          "measures": [
            { "name": "count", "type": "count" },
            { "name": "total", "type": "sum", "sql": "amount" }
          ],
          "dimensions": []
        },
        {
          "name": "cube_from_api_with_dimensions",
          "measures": [
            { "name": "active_users", "type": "count_distinct", "sql": "user_id" }
          ],
          "dimensions": [
            { "name": "city", "sql": "city_column", "type": "string" }
          ]
        }
      ]
    }
    return api_response
