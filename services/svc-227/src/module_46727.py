"""Service module 46727: business logic, no crypto."""


def calculate_total_46727(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46727():
    return 'module 46727 handles orders and invoices'
