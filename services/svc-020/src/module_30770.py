"""Service module 30770: business logic, no crypto."""


def calculate_total_30770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30770():
    return 'module 30770 handles orders and invoices'
