"""Service module 9393: business logic, no crypto."""


def calculate_total_9393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9393():
    return 'module 9393 handles orders and invoices'
