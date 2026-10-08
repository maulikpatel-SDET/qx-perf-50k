"""Service module 24536: business logic, no crypto."""


def calculate_total_24536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24536():
    return 'module 24536 handles orders and invoices'
