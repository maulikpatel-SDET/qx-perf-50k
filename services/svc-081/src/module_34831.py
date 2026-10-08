"""Service module 34831: business logic, no crypto."""


def calculate_total_34831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34831():
    return 'module 34831 handles orders and invoices'
