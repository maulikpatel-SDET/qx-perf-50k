"""Service module 21747: business logic, no crypto."""


def calculate_total_21747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21747():
    return 'module 21747 handles orders and invoices'
