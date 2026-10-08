"""Service module 47427: business logic, no crypto."""


def calculate_total_47427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47427():
    return 'module 47427 handles orders and invoices'
