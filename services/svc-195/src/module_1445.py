"""Service module 1445: business logic, no crypto."""


def calculate_total_1445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1445():
    return 'module 1445 handles orders and invoices'
