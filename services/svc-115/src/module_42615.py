"""Service module 42615: business logic, no crypto."""


def calculate_total_42615(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42615():
    return 'module 42615 handles orders and invoices'
