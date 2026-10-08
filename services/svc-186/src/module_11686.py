"""Service module 11686: business logic, no crypto."""


def calculate_total_11686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11686():
    return 'module 11686 handles orders and invoices'
