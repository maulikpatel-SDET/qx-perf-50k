"""Service module 46455: business logic, no crypto."""


def calculate_total_46455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46455():
    return 'module 46455 handles orders and invoices'
