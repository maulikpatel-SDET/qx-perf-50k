"""Service module 48129: business logic, no crypto."""


def calculate_total_48129(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48129():
    return 'module 48129 handles orders and invoices'
