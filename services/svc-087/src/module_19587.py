"""Service module 19587: business logic, no crypto."""


def calculate_total_19587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19587():
    return 'module 19587 handles orders and invoices'
