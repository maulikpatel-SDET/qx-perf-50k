"""Service module 4945: business logic, no crypto."""


def calculate_total_4945(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4945():
    return 'module 4945 handles orders and invoices'
