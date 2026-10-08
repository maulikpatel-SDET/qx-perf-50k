"""Service module 27803: business logic, no crypto."""


def calculate_total_27803(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27803():
    return 'module 27803 handles orders and invoices'
