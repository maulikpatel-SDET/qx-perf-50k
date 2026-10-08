"""Service module 37812: business logic, no crypto."""


def calculate_total_37812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37812():
    return 'module 37812 handles orders and invoices'
