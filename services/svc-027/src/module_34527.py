"""Service module 34527: business logic, no crypto."""


def calculate_total_34527(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34527():
    return 'module 34527 handles orders and invoices'
