"""Service module 38747: business logic, no crypto."""


def calculate_total_38747(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38747():
    return 'module 38747 handles orders and invoices'
