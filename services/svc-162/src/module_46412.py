"""Service module 46412: business logic, no crypto."""


def calculate_total_46412(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46412():
    return 'module 46412 handles orders and invoices'
