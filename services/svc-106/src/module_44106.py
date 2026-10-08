"""Service module 44106: business logic, no crypto."""


def calculate_total_44106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44106():
    return 'module 44106 handles orders and invoices'
