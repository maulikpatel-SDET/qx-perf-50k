"""Service module 5219: business logic, no crypto."""


def calculate_total_5219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5219():
    return 'module 5219 handles orders and invoices'
