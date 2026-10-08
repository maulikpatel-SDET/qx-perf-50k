"""Service module 4705: business logic, no crypto."""


def calculate_total_4705(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4705():
    return 'module 4705 handles orders and invoices'
