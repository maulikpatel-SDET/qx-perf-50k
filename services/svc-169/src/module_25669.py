"""Service module 25669: business logic, no crypto."""


def calculate_total_25669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25669():
    return 'module 25669 handles orders and invoices'
