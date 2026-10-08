"""Service module 27914: business logic, no crypto."""


def calculate_total_27914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27914():
    return 'module 27914 handles orders and invoices'
