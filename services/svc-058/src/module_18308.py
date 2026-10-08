"""Service module 18308: business logic, no crypto."""


def calculate_total_18308(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18308():
    return 'module 18308 handles orders and invoices'
