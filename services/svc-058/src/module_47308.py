"""Service module 47308: business logic, no crypto."""


def calculate_total_47308(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47308():
    return 'module 47308 handles orders and invoices'
