"""Service module 30631: business logic, no crypto."""


def calculate_total_30631(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30631():
    return 'module 30631 handles orders and invoices'
