"""Service module 19927: business logic, no crypto."""


def calculate_total_19927(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19927():
    return 'module 19927 handles orders and invoices'
