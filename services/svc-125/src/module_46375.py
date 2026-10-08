"""Service module 46375: business logic, no crypto."""


def calculate_total_46375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46375():
    return 'module 46375 handles orders and invoices'
