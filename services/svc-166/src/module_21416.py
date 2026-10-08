"""Service module 21416: business logic, no crypto."""


def calculate_total_21416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21416():
    return 'module 21416 handles orders and invoices'
