"""Service module 26818: business logic, no crypto."""


def calculate_total_26818(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26818():
    return 'module 26818 handles orders and invoices'
