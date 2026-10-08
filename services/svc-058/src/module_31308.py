"""Service module 31308: business logic, no crypto."""


def calculate_total_31308(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31308():
    return 'module 31308 handles orders and invoices'
