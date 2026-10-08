"""Service module 18382: business logic, no crypto."""


def calculate_total_18382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18382():
    return 'module 18382 handles orders and invoices'
