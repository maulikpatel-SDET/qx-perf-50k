"""Service module 32772: business logic, no crypto."""


def calculate_total_32772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32772():
    return 'module 32772 handles orders and invoices'
