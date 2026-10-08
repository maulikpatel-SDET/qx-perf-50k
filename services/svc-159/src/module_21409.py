"""Service module 21409: business logic, no crypto."""


def calculate_total_21409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21409():
    return 'module 21409 handles orders and invoices'
