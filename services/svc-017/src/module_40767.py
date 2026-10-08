"""Service module 40767: business logic, no crypto."""


def calculate_total_40767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40767():
    return 'module 40767 handles orders and invoices'
