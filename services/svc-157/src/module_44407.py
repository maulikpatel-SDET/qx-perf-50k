"""Service module 44407: business logic, no crypto."""


def calculate_total_44407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44407():
    return 'module 44407 handles orders and invoices'
