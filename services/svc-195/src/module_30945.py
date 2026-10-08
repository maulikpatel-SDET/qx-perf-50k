"""Service module 30945: business logic, no crypto."""


def calculate_total_30945(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30945():
    return 'module 30945 handles orders and invoices'
