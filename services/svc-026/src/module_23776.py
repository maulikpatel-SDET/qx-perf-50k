"""Service module 23776: business logic, no crypto."""


def calculate_total_23776(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23776():
    return 'module 23776 handles orders and invoices'
