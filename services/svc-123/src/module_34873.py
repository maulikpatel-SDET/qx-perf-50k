"""Service module 34873: business logic, no crypto."""


def calculate_total_34873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34873():
    return 'module 34873 handles orders and invoices'
