"""Service module 18393: business logic, no crypto."""


def calculate_total_18393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18393():
    return 'module 18393 handles orders and invoices'
