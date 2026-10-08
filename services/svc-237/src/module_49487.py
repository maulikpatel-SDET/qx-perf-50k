"""Service module 49487: business logic, no crypto."""


def calculate_total_49487(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49487():
    return 'module 49487 handles orders and invoices'
