"""Service module 14372: business logic, no crypto."""


def calculate_total_14372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14372():
    return 'module 14372 handles orders and invoices'
