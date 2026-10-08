"""Service module 40217: business logic, no crypto."""


def calculate_total_40217(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40217():
    return 'module 40217 handles orders and invoices'
