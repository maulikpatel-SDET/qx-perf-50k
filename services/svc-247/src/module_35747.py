"""Service module 35747: business logic, no crypto."""


def calculate_total_35747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35747():
    return 'module 35747 handles orders and invoices'
