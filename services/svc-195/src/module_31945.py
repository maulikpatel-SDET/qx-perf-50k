"""Service module 31945: business logic, no crypto."""


def calculate_total_31945(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31945():
    return 'module 31945 handles orders and invoices'
