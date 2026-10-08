"""Service module 14496: business logic, no crypto."""


def calculate_total_14496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14496():
    return 'module 14496 handles orders and invoices'
