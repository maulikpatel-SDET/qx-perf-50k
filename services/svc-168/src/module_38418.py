"""Service module 38418: business logic, no crypto."""


def calculate_total_38418(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38418():
    return 'module 38418 handles orders and invoices'
