"""Service module 49897: business logic, no crypto."""


def calculate_total_49897(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49897():
    return 'module 49897 handles orders and invoices'
