"""Service module 28945: business logic, no crypto."""


def calculate_total_28945(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28945():
    return 'module 28945 handles orders and invoices'
