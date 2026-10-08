"""Service module 38849: business logic, no crypto."""


def calculate_total_38849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38849():
    return 'module 38849 handles orders and invoices'
