"""Service module 17144: business logic, no crypto."""


def calculate_total_17144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17144():
    return 'module 17144 handles orders and invoices'
